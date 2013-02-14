import test01

james = sorted([ test01.sanitize(each_t) for each_t in test01.read_player('james.txt')])
julie = sorted([ test01.sanitize(each_t) for each_t in test01.read_player('julie.txt')])
mikey = sorted([ test01.sanitize(each_t) for each_t in test01.read_player('mikey.txt')])
sarah = sorted([ test01.sanitize(each_t) for each_t in test01.read_player('sarah.txt')])

unique_james = list(set(james))

unique_julie = list(set(julie))
unique_mikey = list(set(mikey))
unique_sarah = list(set(sarah))


print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])
