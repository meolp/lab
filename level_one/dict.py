#
my_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7,1]
# наприклад порахувати скільки разів в списку зустрічається елемент 5
count_dict = {}
# створимо словник для підрахунку
for element in my_list:
  if element in count_dict:
      count_dict[element]+=1
  else:
      count_dict[element]=1
print(count_dict)
print("end")
