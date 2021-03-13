dem_list = [2]
num_list = [3]

for x in range(0,999):
    new_den = 0
    for num in num_list:
        new_den = new_den+num
    dem_list.append(new_den+2)
    prev_num = dem_list[len(num_list)-1]
    num_list.append(new_den+2+prev_num)



num_gr = 0
for x in range (0,1000):
    if len(str(num_list[x]))>len(str(dem_list[x])):
        num_gr = num_gr+1
        
print (num_gr)