numbers = [10, 20, 30, 40, 50]
total=sum(numbers)
average = (total/len(numbers))
print(average)

count=0
for i in numbers:
    if i>average:
        count+=1
print(count)
