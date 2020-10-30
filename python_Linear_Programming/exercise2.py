import pulp

# 參數
x = pulp.LpVariable("x", lowBound=0, upBound=None, cat="Integer")
y = pulp.LpVariable("y", lowBound=0, upBound=None, cat="Integer")

# 最大值
prob = pulp.LpProblem("problemName", pulp.LpMaximize)

# 目標
prob.setObjective(200000 * x + 80000 * y)

# 加入限制條件
prob += 3000 * x + 900 * y <= 75000
prob += -5 * x + y <= 0
prob += 1 * x <= 15
prob += 1 * x >= 5

# print(prob)

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

