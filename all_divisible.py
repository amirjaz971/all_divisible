target_num=int(input('enter target number: '))

num=int(input('how many numbers do you want to enter?: '))
not_divisible=''
are_divisible=''
numbers=input('enter other numbers in one line: ').split()[:num]
numbers_list=[]
divisible_num=0
for i in numbers:
    if target_num%int(i)!=0:
        i=str(i)
        not_divisible+=i+' '
        
    else:
        i=str(i)
        are_divisible+=i+' '
        divisible_num+=1


        
if divisible_num==num:
    print(f'all of the numbers are divisible to {target_num}')
else:
    print(f'Not all of the numbers are divisible to {target_num}')

print(f'the numbers which are divisible to {target_num} are:{are_divisible}')
print(f'the numbers which are not divisible to {target_num} are:{not_divisible}')

        

