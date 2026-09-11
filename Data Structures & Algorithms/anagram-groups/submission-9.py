class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for st in strs:
            arr = [0] * 26

            for c in st:
                arr[ord(c) - ord('a')] += 1

            key = tuple(arr)

            if key not in dic:
                dic[key] = []

            dic[key].append(st)

        return list(dic.values())

            
        