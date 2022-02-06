#порахувати за допомогою словника скільки разів елемент повторюється в списку

my_list=[1,1,1,2,2,3,4,5,6,6,7,7,7,7,7,1,1]
value_to_count = 1
#наприклад порахувати скільки разів в списку зустрічається елемент 5
count_dict={value_to_count:0}
#створимо словник для підрахунку
for element in my_list:
    if element ==value_to_count :
        count_dict[value_to_count]+=1
        
print (count_dict)

