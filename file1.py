# # import pytest
# # import random
# # from tenacity import retry
# #
# # from tenacity import Retrying, RetryError, stop_after_attempt
# # from tenacity import AsyncRetrying, retry_if_result
# #
# # # async def function():
# # #    async for attempt in AsyncRetrying(retry=retry_if_result(lambda x: x < 3)):
# # #        with attempt:
# # #            result = 1  # Some complex calculation, function call, etc.
# # #        if not attempt.retry_state.outcome.failed:
# # #            attempt.retry_state.set_result(result)
# # #    return result
# #
# #
# # from tenacity import Retrying, RetryError, stop_after_attempt
# #
# # try:
# #    for attempt in Retrying(stop=stop_after_attempt(3)):
# #        with attempt:
# #            raise Exception('My code is failing!')
# # except RetryError:
# #    pass
# #
# # #
# # # def func(x):
# # #   if x == 5:
# # #     raise ValueError("x must be a value other than 5")
# # #   return x
# # #
# # # def test_func():
# # #   with pytest.raises(ValueError, match="x must be a value other than 5"):
# # #     func(5)
# # #
# # # #func(5)     # Raises an exemption
# # #
# # # test_func()
# # import tenacity
# # from tenacity import *
# #
# # # @retry(wait=wait_fixed(2) , stop=stop_after_attempt(5))
# # # def exception_function():
# # #     print("exception time")
# # #     # tenacity.Retrying()
# # #     raise Exception
# # #
# # # exception_function()
# #
# #
# # @retry(stop=(stop_after_delay(1)), retry=retry_if_exception_type((IOError, ConnectionError)))
# # def func1(x):
# #     if x==1:
# #         print("IO Error x = 1")
# #         raise IOError
# #     elif x==2:
# #         print("Connection Error x = 2")
# #         raise ConnectionError
# #     elif x == 3:
# #         print('Type Error x = 3 ')
# #         raise TypeError
# #     else:
# #         return 'Success'
# #
# #
# # func1(1)
# import tenacity
# from tenacity import *
# import time
#
#
# from tenacity import AsyncRetrying, retry_if_result
#
#
# def func2():
#     return 5
#
#
# tenacity.retry(func2(), )
#
#
# async def function1():
#
#    async for attempt in AsyncRetrying(retry=retry_if_result(lambda x: x < 3)):
#        with attempt:
#            result = 1  # Some complex calculation, function call, etc.
#        if not attempt.retry_state.outcome.failed:
#            attempt.retry_state.set_result(result)
#    return result
#
# function1()
# tenacity.Retrying
# # @retry(wait=wait_exponential(multiplier=1, min=4, max=10))
# # def wait_exponential_1():
# #     print("Wait 2^x * 1 second between each retry starting with "
# #           "4 seconds, then up to 10 seconds, then 10 seconds afterwards")
# #
# #     raise Exception
# #
# #
# # wait_exponential_1()

def total_fruits(*args, **kwargs):
    #print(kwargs, type(kwargs))
    #print(args, type(args))
    for i in kwargs:
        print("the key {} and the value {}".format(i, kwargs[i]))
    for j in args:
        print(j)


total_fruits(banana=5, mango=7, apple=8)
total_fruits(1, 2, 3, 4, 13123, 55)

