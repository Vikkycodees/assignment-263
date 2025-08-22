from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    
    for word in words:
        # Sort the word to create a common key
        key = "".join(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
