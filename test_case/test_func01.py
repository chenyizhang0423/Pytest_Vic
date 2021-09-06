import pytest,os,allure


# # 1: 定义函数类型---测试用例
# def test_tc01():
#     assert 1+1 ==2
# def test_tc02():
#     assert 1+1 ==3

@allure.feature("登录模块")  # 一级标签
# 2: 封装测试类
class TestLogin:
    def setup_class(self):
        print("执行测试类之前需要执行的初始化操作")

    @allure.story("登录login01")   # 二级标签
    @allure.title("login01")      # 每个用例都会带
    #@pytest.mark.parametrize('a', [1,2,3])
    @pytest.mark.parametrize('a,b',[(1,2),(3,4),(5,6)])
    def test_login01(self,a,b):
        print("------test01------")
        assert a + 1 == b

    @allure.story("登录login02")   # 二级标签
    @allure.title("login02")
    def test_login02(self):
        print("------test02------")
        assert 1+1 == 3

    def teardown_class(self):
        print("执行测试类之后需要执行的清除操作")

@allure.feature("购物模块")  # 一级标签
# 2: 封装测试类
class TestShopping:
    @allure.story("shopping")   # 二级标签
    @allure.title("shopping01")
    def test_shopping(self):
        print("------test02------")
        assert 1+1 == 3



if __name__ == '__main__':
        # 需要显示打印信息的话，需要加参数-s
        # 1： --alluredir : 存放用于生成allure的临时文件
        pytest.main(['test_func01.py','-s','--alluredir','../report/tmp'])
        # 2： allure generate allure报告  =>cmd命令， 此时需要os模块
        # os.system('allure generate 用于生成报告的临时文件的所在路径 -o 生成的allure要存放的路径')
        os.system('allure generate ../report/tmp -o ../report/report --clean')
