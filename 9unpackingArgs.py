def health_cal(age,dm_age,smoke):
    ans = age+dm_age + smoke /5
    print(ans)

test_args = [1,2,3]
health_cal(test_args[0], test_args[1],test_args[2])
'''unpacking arg is there'''
health_cal(*test_args)