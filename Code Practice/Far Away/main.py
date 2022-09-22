# cook your dish here
def get_max_distance(array_a, ab_limit):
    """
    Get maximum distance from array A with limit of integer M
    :param:
    array_a: Array
    ab_limit: integer M
    :output: max_distance
    complexity O(2N) where N is length of array_a
    """
    
    #populate array B
    array_b = []
    a_length = len(array_a)
    
    for j in range(a_length):
        a_val = array_a[j]
        if a_val <= ab_limit//2:
            array_b.append(ab_limit)
        else:
            array_b.append(1)
    
    #get max distance
    max_distance = 0
    for k in range(a_length):
        distance = abs(array_a[k] - array_b[k])
        max_distance += distance
        
    #Output
    return max_distance
    

    
#number of test cases
test_cases = input()

#run all test cases
for i in range(int(test_cases)):
    
    #Get input
    line_1 = input().split(' ')
    line_2 = input().split(' ')
    
    #normalise input
    ab_limit = int(line_1[1])
    #Convert string array into int array, O(N)
    array_a = [int(str_val) for str_val in line_2]
    
    print(get_max_distance(array_a, ab_limit))
    