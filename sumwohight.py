arrtest = [6,2,1,8,10]
#arrtest = [1]
#arrtest = []
#arrtest = None

def sum_arry(arr):
    if(arr is None) or (len(arr) ==1 ) or (not arr):
        return print(0)
    else:
        h = 0
        l = 0
        sum_result = 0
        for x in arr:
            sum_result += x
        #sum_result = 1
        return print(sum_result)


sum_arry(arrtest)