"""
输入某年某月某日，判断这一天是这一年的第几天？

闰年有以下特征：

1. 闰年是能够被4整除的年份。例如，2020年、2024年、2028年都是闰年。

2. 除了能够被4整除之外，闰年还需要满足以下条件之一：
   - 不能被100整除。例如，2004年、2008年是闰年，因为它们能够被4整除但不能被100整除。
   - 或者能够被400整除。例如，2000年是闰年，因为它能够被400整除。

综上，能被 400 整除，或者 能被 4 整除，但不能被 100 整除

根据这些特征，闰年的出现是为了调整日历与地球公转周期的不精确性之间的差异。一年的长度是大约365.24天，为了保持日历与季节的同步，我们需要添加额外的一天（2月29日）来弥补每年的多余时间。

需要注意的是，闰年的定义是根据公历（Gregorian calendar）而言的。其他历法系统可能有不同的规则和特征来确定闰年。


"""
year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
day = int(input('请输入日:'))

# 用元祖列举每个月的天数，或者存储当月总天数
# 如果是 1 月，则只加天数即可
# 如果是 2 月，则需要算上 1 月累计的天数 + 日期数
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

total_count = 0
if 0 < month <= 12:
    total_count = months[month - 1]
else:
    print('data error')

total_count += day

is_leap = False

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    """判断是否是闰年"""
    is_leap = True

if is_leap and month > 1:
    """如果是闰年，那么二月要变成 29 天"""
    total_count += 1
print('it is the %dth day', total_count)
