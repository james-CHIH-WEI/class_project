import pulp

# 參數
x = pulp.LpVariable("x", lowBound=0, upBound=None, cat="Continuous")
y = pulp.LpVariable("y", lowBound=0, upBound=None, cat="Continuous")
z = pulp.LpVariable("z", lowBound=0, upBound=None, cat="Continuous")
c = pulp.LpVariable("c", lowBound=0, upBound=None, cat="Continuous")

# 最大值
prob = pulp.LpProblem("problemName", pulp.LpMinimize)

# 目標
prob.setObjective(0.12 * x + 0.09 * y + 0.11 * z + 0.04 * c)

total_weight = 50

# 加入限制條件
prob += c >= total_weight * 0.15
prob += x + y >= total_weight * 0.45
prob += y + z <= total_weight * 0.3
prob += x + y + z + c == total_weight

# print(prob)

# 開始計算
status = prob.solve()
print((status, pulp.LpStatus[status]))

# 結果
print(
    "C-30=",
    pulp.value(x),
    ",  C-92=",
    pulp.value(y),
    ",  D-21=",
    pulp.value(z),
    ",  E-11=",
    pulp.value(c),
    ",  result=",
    pulp.value(prob.objective),
)

