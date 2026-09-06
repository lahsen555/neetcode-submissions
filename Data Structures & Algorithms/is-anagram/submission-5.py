class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        dics = {}
        dicts = {}
        for i in ls:
            dics[i] = 0
        for i in lt:
            dicts[i] = 0
        for i in ls:
            dics[i] += 1
        for i in lt:
            dicts[i] += 1

        return dics == dicts