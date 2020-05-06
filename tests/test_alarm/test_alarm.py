# -*- coding: utf-8 -*-
"""
Project: EverydayWechat-Github
Creator: DoubleThunder
Create time: 2019-07-11 12:03
Introduction:
"""
from tests import BaseTestCase
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from everyday_wechat.utils import config
from everyday_wechat.utils.itchat_helper import (
    init_alert_config,
)

class TestJobModel(BaseTestCase):
    def test_alarm(self):
        """
        测试定时任务。
        :return:
        """
        init_alert_config()  # 初始化所有配置内容
        alarm_dict = config.get('alarm_info').get('alarm_dict')
        print(alarm_dict)
        scheduler = BlockingScheduler()
        for key, value in alarm_dict.items():
            scheduler.add_job(send_alarm_msg, 'cron', hour=value['hour'],
                              minute=value['minute'])
        scheduler.start()

        print('已开启定时发送提醒功能...')
        print(scheduler.get_jobs())

def send_alarm_msg():
    """ 发送定时提醒 """
    print('\n启动定时自动提醒...')
