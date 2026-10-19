# ============================================
# 复利计算程序
# 公式：FV = PV × (1 + r)^n
# ============================================

# 本金（Present Value）：初始存入的金额
pv = 10000

# 年利率：5% 转换为小数 0.05
annual_rate = 0.05

# 存款年数
years = 3

# 每年复利次数：题目要求每年复利 1 次
compound_per_year = 1

# 每期利率 = 年利率 ÷ 每年复利次数
# 这里每年复利1次，所以每期利率 = 0.05 ÷ 1 = 0.05
period_rate = annual_rate / compound_per_year

# 总复利期数 = 年数 × 每年复利次数
# 这里 = 3 × 1 = 3 期
total_periods = years * compound_per_year

# 计算本息和（终值 FV）
# FV = PV × (1 + r)^n
# 即：本息和 = 本金 × (1 + 每期利率) 的 总期数 次方
fv = pv * (1 + period_rate) ** total_periods

# 输出结果，保留两位小数
# round(数值, 2) 表示保留2位小数
print(f"本金：{pv} 元")
print(f"年利率：{annual_rate * 100}%")
print(f"存款年限：{years} 年")
print(f"每年复利次数：{compound_per_year} 次")
print(f"最终本息和：{round(fv, 2)} 元")