# import random
# import string
# import pandas
# import time
#
# data_base = {}
#
# def policy_creator():
#     letter_list = list(string.ascii_uppercase)
#     digits_list = list(string.digits)
#
#     policy_letters = []
#     policy_digits = []
#
#     for i in range(3):
#         policy_letters.append(random.choice(letter_list))
#
#     for j in range(8):
#         policy_digits.append(random.choice(digits_list))
#
#     policy_start = ''.join(policy_letters)
#     policy_end = ''.join(policy_digits)
#
#     full_policy = policy_start + '-' + policy_end
#
#     return full_policy
#
#
# def db_appending():
#     new_policy = policy_creator()
#     data_base[(len(data_base))] = new_policy
#     return
#
# time_1 = time.time()
# for i in range(12):
#     db_appending()
#
# print(data_base)
#
# time_2 = time.time()
#
# print(time_2-time_1)
