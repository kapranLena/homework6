# def my_function(**dict):
#     return (dict)
# func_res = my_function([var1] == 2, var2 = 'two', var3 = 5, var4 = 'hello')
# print(func_res)
# якщо намагатися списати у my_function ключі типу стрічки, цифри, то вибивало Error. то прийшлось робити так
def fun(**kwargs):
    print(kwargs)

dict = {(1,2): 'one two', 3: 'tree', 'run': '345'}
for key, value in dict.items():
    if type(key) is str:
        print(key, value)
    else:
        print('not found')
