class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for words in strs:
            key = "".join(sorted(words))
            group.setdefault(key,[]).append(words)
        return list(group.values())
        