pow = 5
nums = []


for i in range(2, 1_000_000):
  str_i = str(i)
  _sum = 0
  for j in str_i:
    _sum += int(j) ** pow
  
  if _sum == i:
    nums.append(i)


print(nums)
print(sum(nums))
