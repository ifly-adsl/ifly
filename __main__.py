import __config__ as cf
from __global__ import GlobalVariables

import os


cf.init()

cf.glv_set(GlobalVariables.global_tmp, r'./tmp')
cf.glv_set(GlobalVariables.MERGE_STATIC_PATH,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), "DZ_Merge_Static.csv"))
cf.glv_set(GlobalVariables.CLEAN_FILE_PATH,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"Sector_Clean"))
cf.glv_set(GlobalVariables.SAVE_CGI_INFO_PATH,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"CGI_Clean"))
cf.glv_set(GlobalVariables.SAVE_PATH_HIGHLOAD,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"DZ_0512_0624_highload_cgi_list.csv"))
cf.glv_set(GlobalVariables.SAVE_PATH_ABNORMAL,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"DZ_0512_0624_abnormal_cgi_list.csv"))
cf.glv_set(GlobalVariables.save_forecast_file_rootdir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r'Forecast'))

cf.glv_set(GlobalVariables.caculate_forecast_sector_license_save_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"扇区需求计算结果"))
cf.glv_set(GlobalVariables.extend_sector_by_forecast_save_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"预测扩容扇区"))
cf.glv_set(GlobalVariables.decreased_sector_by_forecast_save_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"预测减容扇区"))
cf.glv_set(GlobalVariables.recent_load_select_save_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"基于近期负载特征优化的扩容扇区"))
cf.glv_set(GlobalVariables.save_threshold_extend_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"设定阈值的扩容结果"))
cf.glv_set(GlobalVariables.save_threshold_decrease_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r"设定阈值的减容结果"))
cf.glv_set(GlobalVariables.schedule_dir,
           os.path.join(cf.glv_get(GlobalVariables.global_tmp), r'schedule'))

cf.glv_set(GlobalVariables.days_threshold_for_extend, 5)
cf.glv_set(GlobalVariables.reduce_volume_factor, 1.0)


def complete_config():
    """
    根据传入的参数完善相关配置
    :return:
    """
    # 历史静态表所在的根目录
    cf.glv_set(GlobalVariables.STATIC_DIR_PATH, r'/home/wm775825/test/静态表')
    # 最新静态表的路径
    cf.glv_set(GlobalVariables.STATIC_FILE_PATH, r'/home/wm775825/test/静态表/0512-更新-静态表.csv')
    # 小区PRB资源配置表路径
    cf.glv_set(GlobalVariables.PRB_STATIC_FILE_PATH, r'/home/wm775825/test/Prb_Static.csv')
    # 所有动态表所在的根目录
    cf.glv_set(GlobalVariables.DYNAMIC_FILE_PATH, r'/home/wm775825/test/动态表')

    # 动态表的起始时间
    cf.glv_set(GlobalVariables.dynamic_start_date, "2019-05-12 00:00")
    # 动态表的持续天数
    cf.glv_set(GlobalVariables.dynamic_days, 44)
    # 使用的训练集的天数
    cf.glv_set(GlobalVariables.training_days, 37)
    # 预测的起始时间
    cf.glv_set(GlobalVariables.forecast_start_date, "2019-06-18 00:00")
    # 预测的天数
    cf.glv_set(GlobalVariables.forecast_days, 7)

    # 近期负载特征迁移位置（即有效预测起始时间）
    cf.glv_set(GlobalVariables.start_analyze_date, '2019-06-18 00:00')
    # 近期负载特征提取天数（即有效预测的天数）
    cf.glv_set(GlobalVariables.analyze_days, 7)


def main():
    complete_config()
    # TODO：依次调用各个子包下的入口函数
    # TODO：具体模块的导入要在complete_config函数后边
    from forecast.Data_Preprocessing_Forecast_Main import data_preprocessing_and_forecast
    from analysis.gen_list_by_forecast import extend_decrease_by_forecast
    from analysis.gen_list_by_recent import extend_by_recent_feature_extract
    from analysis.threshold_process import final_extend_decrease_by_threshold
    # from schedule.schedule import main as sche

    data_preprocessing_and_forecast()
    extend_decrease_by_forecast()
    extend_by_recent_feature_extract()
    final_extend_decrease_by_threshold()

    # 以小时为单位生成调度清单
    # sche()


if __name__ == '__main__':
    main()
