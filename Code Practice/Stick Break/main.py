# cook your dish here
#number of test cases
test_cases = input()

#Algorithm starts here
def break_stick(stick_length, stick_parts):
    
    #get min_value
    min_val = stick_length%stick_parts
    if min_val > 0:
        return 1
    else:
        return 0
    
    
#run all test cases
for i in range(int(test_cases)):

    #Create Array for string based input 
    line_1 = input().split(' ')
    
    stick_length = int(line_1[0])
    stick_parts = int(line_1[1])
    
    print(break_stick(stick_length, stick_parts))
    