total_number = 0

for n in range(1, 101): #in case of using range 1-100 means 1-99 so we need to assume 1-101
  if n % 2 == 0:
    total_number +=n
print(total_number)