start = 1
end = 500
for num in range(start, end+1):
  if num % 7 == 0 and num % 11 == 0:
    print(num)