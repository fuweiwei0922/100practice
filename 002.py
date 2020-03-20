# 题目 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

profit = int(input('please input the profit of this month\n'))


commission_rate_1 = 0
commission_rate_2 = 0
commission_rate_3 = 0
commission_rate_4 = 0
commission_rate_5 = 0
commission_rate_6 = 0

if profit <= 100000:
	commission_rate_1 = 0.1
elif  profit <= 200000:
	commission_rate_2 = 0.75
elif profit<= 4000000:
	commission_rate_3 = 0.05
elif profit <= 600000:
	commission_rate_4 = 0.03
elif profit <=1000000:
	commission_rate_5 = 0.015
else:
	commission_rate_6 = 0.001

total_commission = int(100000*commission_rate_1+100000*commission_rate_2+200000*commission_rate_3+200000*commission_rate_4+400000*commission_rate_5+(profit-1000000)*commission_rate_6)

print(f"Your commission for this month is {total_commission} YUAN.")