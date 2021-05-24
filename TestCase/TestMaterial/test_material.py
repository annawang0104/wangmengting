"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""

import cmd
import logging
import os
import sys

import allure
import pytest

from Base.ReadfilePath import get_file_path
from Util.apiSendCheck import api_send_check
from Util.readDatamethod import ReadFileData

file = get_file_path("TestCase","TestMaterial","material.json")

case_dict = ReadFileData().load_json(file_path=file)



@allure.feature(case_dict["scenarioName"])
class TestMaterial:
    @pytest.mark.parametrize("case_data", case_dict["steps"])
    @allure.story("素材库")
    # @pytest.mark.flaky(reruns=1, reruns_delay=3)
    def test_materail(self,case_data,login_in_load):
        """

        :param case_data: 单个测试用例数据
        :return:
        """
        # 发送测试请求
        api_send_check(case_data)


if __name__ == '__main__':
    root_dir = os.path.dirname(__file__)
    pytest.main('-s', '-q','--alluredir',"/Users/tezign/PycharmProjects/api_test_wmt/Result")
    md = 'allure generate ./Report/{}/allure-result -o ./Report/{}/allure-report --clean'
    logging.info("命令行执行cmd:{}".format(cmd))

    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败！'.format(cmd))
        sys.exit()
        # 打印url，方便直接访问

