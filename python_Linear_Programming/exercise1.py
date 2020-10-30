import pulp

# 參數
x = pulp.LpVariable("x", lowBound=0, upBound=None)
y = pulp.LpVariable("y", lowBound=0, upBound=None)

# 最小值
prob = pulp.LpProblem("problemName", pulp.LpMinimize)

# 目標
prob.setObjective(0.1 * x + 0.15 * y)

# 加入限制條件
prob += 5 * x + 10 * y >= 45
prob += 4 * x + 3 * y >= 24
prob += 0.5 * x >= 1.5

print(prob)

# 開始計算
status = prob.solve()
print((status, pulp.LpStatus[status]))

# 結果
print(
    "x=",
    pulp.value(x),
    ",  y=",
    pulp.value(y),
    ",  result=",
    pulp.value(prob.objective),
)

