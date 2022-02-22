"""
作者:evita
日期:2022年02月22日
"""
#4、定义一个start.py ，启动文件展示最终存款金额
import select_money
import send_money
if __name__ == '__main__':
    send_money.sendmoney()
    select_money.selectmoney()