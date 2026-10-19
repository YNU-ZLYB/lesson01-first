# ============================================
# 复利 vs 单利 对比表
# 复利公式：FV = PV × (1 + r)^n
# 单利公式：FV = PV × (1 + r × n)
# ============================================

print("=== 复利 vs 单利 对比表 ===")

# 1. 输入本金
pv = float(input("请输入本金（元）："))

# 2. 输入年利率，校验不能为负数
while True:
    annual_rate = float(input("请输入年利率（如 5 表示 5%）："))
    if annual_rate < 0:
        print("利率不能为负，请重新输入。")
    else:
        break

# 百分比转小数：5 → 0.05
r = annual_rate / 100

# 3. 对比年限列表
years_list = [10, 20, 30]

# 4. 打印表头
# \t 是制表符，用来对齐列
print(f"\n{'年限':<6}{'复利终值':<15}{'单利终值':<15}{'差额':<15}")
print("-" * 50)

# 5. 逐行计算并输出
for n in years_list:
    # 复利终值：FV = PV × (1 + r)^n
    fv_compound = pv * (1 + r) ** n

    # 单利终值：FV = PV × (1 + r × n)
    fv_simple = pv * (1 + r * n)

    # 差额 = 复利 - 单利
    diff = fv_compound - fv_simple

    # 输出一行，保留两位小数
    print(f"{n:<8}{fv_compound:<15.2f}{fv_simple:<15.2f}{diff:<15.2f}")