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
        scheduler = BlockingScheduler()
        for key, value in alarm_dict.items():
            if 'days' in value:
                scheduler.add_job(send_alarm_msg, 'interval', [key], days=value['days'], start_date=value['start_time'],
                              id=key, misfire_grace_time=600)
            elif 'day' in value:
                scheduler.add_job(send_alarm_msg, 'cron', [key], day=value['day'], hour=value['hour'],
                              minute=value['minute'], id=key, misfire_grace_time=600)
            else:
                scheduler.add_job(send_alarm_msg, 'cron', [key], hour=value['hour'],
                              minute=value['minute'], id=key, misfire_grace_time=600)
        scheduler.start()

        print('已开启定时发送提醒功能...')
        print(scheduler.get_jobs())

def send_alarm_msg(key):
    """ 发送定时提醒 """
    print('\nyang')
