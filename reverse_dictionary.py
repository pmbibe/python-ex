def reverse_dictionary(d):
    a={}
    k=0
    list_keys = []
    list_values = []
    for key,value in d.items():
        list_keys.append(key)
        for values in value:
            list_values.append(values)
    list_values_af = set(list_values)
    for j in list_values_af:
        for i in range(len(list_values)):
            if list_values[i] == j:
                k = k + 1
                a[j] = k
        k = 0
    for key_a,value_a in a.items():
        a[key_a] = list()
        while value_a > 0:
            for key,value in d.items():
                if key_a in d[key]:
                    a[key_a].append(key)
                    value_a = value_a - 1

    print(a)
d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)
