# ============================================
# 交互式复利计算程序
# 公式：FV = PV × (1 + r)^n
# ============================================

print("=== 复利计算器 ===")

# 1. 输入本金（PV）
# float() 将用户输入的字符串转成小数
while True:
    printer = float(input("请输入本金（元）："))
    if printer < 0:
        # 输入负数时提示并继续循环（重输）
        print("本金不能为负，请重新输入。")
    else:
        # 输入合法，跳出循环
        break

# 2. 输入年利率（r），并校验不能为负数
# while True 循环：只要输入不合法就一直要求重输
while True:
    annual_rate = float(input("请输入年利率（如 5 表示 5%）："))
    if annual_rate < 0:
        # 输入负数时提示并继续循环（重输）
        print("利率不能为负，请重新输入。")
    else:
        # 输入合法，跳出循环
        break

# 将百分比转成小数：5 → 0.05
annual_rate = annual_rate / 100

# 3. 输入存款年限
years = int(input("请输入存款年限（年）："))

# 4. 每年复利次数（默认 1 次）
compound_per_year = 1

# 5. 计算每期利率和总期数
period_rate = annual_rate / compound_per_year
total_periods = years * compound_per_year

# 6. 计算本息和：FV = PV × (1 + r)^n
fv = pv * (1 + period_rate) ** total_periods

# 7. 输出结果，保留两位小数
print("\n=== 计算结果 ===")
print(f"本金：{pv} 元")
print(f"年利率：{annual_rate * 100}%")
print(f"存款年限：{years} 年")
print(f"每年复利次数：{compound_per_year} 次")
print(f"最终本息和：{round(fv, 2)} 元")
