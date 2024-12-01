class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        answer = 1
        i = 2
        while i*1 < num:
            if num % i == 0: answer += 1 + num//i
            i += 1
        if i*1 == num: answer += i
        return answer == num
