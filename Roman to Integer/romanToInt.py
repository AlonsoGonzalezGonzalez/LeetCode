class Solution(object):
    def romanToInt(self, s):
        romans={'I':1,'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
        ans=0
        for i in range(len(s)):
            if i+1 < len(s) and romans.get(s[i]) < romans.get(s[i+1])  :
                ans-=romans.get(s[i])
            else:
                ans+=romans.get(s[i])
        return ans