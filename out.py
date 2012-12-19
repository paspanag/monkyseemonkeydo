import random
import copy
random.seed()

value_hash = {chr(n+96):n for n in range(1,27)}
rev_value_hash = {n:chr(n+96) for n in range(1,27)}

def mimer(input_list,output_list,transform_list,value_hash,rev_value_hash):
    
   # print "---------"
   # print input_list
   # print output_list
    remain_list = copy.deepcopy(output_list)
    done_list = []
    result_list = []

    while(len(remain_list)):
        out_rand = random.choice(remain_list)
        in_rand = random.choice(input_list)
        trans_rand = random.choice(transform_list)
        transformed = transform(in_rand,trans_rand)
        
        while(calculate_difference(out_rand,transformed,value_hash)):
            trans_rand = random.choice(transform_list)
            transformed = transform(in_rand,trans_rand,)
        
        remain_list.remove(out_rand)
        done_list.append(out_rand)
        result_list.append((out_rand,in_rand,trans_rand))

    transform_func = to_func(input_list,output_list,result_list)
    return transform_func

def to_func(input_list,output_list,transform_list):
    final_func = []
    for output in output_list:
        for indiv_func in transform_list:
            if output == indiv_func[0]:
                input_ind = input_list.index(indiv_func[1])
                transform_value = indiv_func[2]
                final_func.append((input_ind,transform_value))
    
    return final_func

def fin_transform(input,transfunc_list):
    retval = []
    for transfunc in transfunc_list:
        retval.append(transform(input[transfunc[0]],transfunc[1]))
    return retval

def calculate_difference(first_letter,second_letter,value_hash):
    return abs(value_hash[first_letter]-value_hash[second_letter])

def transform(letter,transform_value):
    value_of_letter = value_hash[letter]
    
    new_value = value_of_letter + transform_value

    if new_value > 26:
        new_value = new_value - 26
    if new_value < 0:
        new_value = new_value + 26
    if new_value == 0:
        return letter
    
    return rev_value_hash[new_value]

if __name__ == "__main__":
    alpha_to_val = {chr(n+96):n for n in range(1,27)}
    val_to_alpha = {n:chr(n+96) for n in range(1,27)}
    tf_list = [n for n in range(-26,27)]

    print "===="
    print "input args"
    print alpha_to_val
    print val_to_alpha
    print tf_list
    print "===="

    results = []
    num = 0
    while(num != 5):
        result_func = mimer(['a','b','c'],['a','b','d'],tf_list,alpha_to_val,val_to_alpha)
        if result_func in results:
            pass
        else:
            num = num + 1
            results.append(result_func)
            print num
            print result_func
    
    print results
  
    print "=======run app========="

    input_list = [['a','b','c'],['x','y','z'],['w','e','r']]
    for input_set in input_list:
        print "-------------------------------"
        print input_set
        print "-------------------------------"
        for res in results:
            print "-=-=-=-=-="
            print res
            print fin_transform(input_set,res)
