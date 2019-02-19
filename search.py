import json

path = input('print the path to the file: ')

try:
    file = open(path)
except FileNotFoundError:
    print('your path is wrong')
js = json.loads(file.read())

def all_endpoints(structure):
    strr_type = type(structure)
    endpoints = {}
    if not (strr_type == list or strr_type == set or strr_type == dict or strr_type == tuple):
        pass
    elif strr_type == list or strr_type == set or strr_type == tuple:
        for elem in structure:
            temp_dict = all_endpoints(elem)
            for endpoint in temp_dict:
                if endpoint in endpoints:
                    endpoints[endpoint] += temp_dict[endpoint]
                else:
                    endpoints[endpoint] = temp_dict[endpoint]
    elif strr_type == dict:
        for elem in structure:
            if elem in endpoints:
                endpoints[elem] += 1
            else:
                endpoints[elem] = 1
            temp_dict = all_endpoints(structure[elem])
            for endpoint in temp_dict:
                if endpoint in endpoints:
                    endpoints[endpoint] += temp_dict[endpoint]
                else:
                    endpoints[endpoint] = temp_dict[endpoint]
    else:
        print('err')
    return endpoints

def find_endpoint(structure, to_go):
    strr_type = type(structure)
    if not (strr_type == list or strr_type == set or strr_type == dict or strr_type == tuple):
        pass
    elif strr_type == list or strr_type == set or strr_type == tuple:
        if to_go in structure:
            return structure[to_go]
        else:
            for elem in structure:
                if find_endpoint(elem, to_go) == None:
                    pass
                else:
                    return find_endpoint(elem, to_go)
    elif strr_type == dict:
        if to_go in structure:
            return structure[to_go]
        else:
            for elem in structure:
                if find_endpoint(structure[elem], to_go) == None:
                    pass
                else:
                    return find_endpoint(structure[elem], to_go)
    else:
        print('err')
    return None

def find_all_endpoints(structure, to_go, prew_result = []):
    strr_type = type(structure)
    result = prew_result
    if not (strr_type == list or strr_type == set or strr_type == dict or strr_type == tuple):
        pass
    elif strr_type == list or strr_type == set or strr_type == tuple:
        if to_go in structure:
            result.add(structure[to_go])
            for elem in structure:
                result = find_all_endpoints(elem, to_go, result)
        else:
            for elem in structure:
                result = find_all_endpoints(elem, to_go, result)
    elif strr_type == dict:
        if to_go in structure:
            result.append(structure[to_go])
            for elem in structure:
                result = find_all_endpoints(structure[elem], to_go, result)
        else:
            for elem in structure:
                result = find_all_endpoints(structure[elem], to_go, result)
    else:
        print('err')

    # print(result)
    # input()
    return result

print('Enter to exit\n\n')
while True:
    to_go = input('print where you want to go: ')
    if not to_go:
        break

    endpoints = all_endpoints(js)
    if to_go not in endpoints:
        print("there isn't such endpoint")
        check = input("do you want to see all endpoints?\nany charecter for yes, Enter for no: ")
        if check:
            for endpoint in endpoints:
                print(endpoint)

    else:
        if endpoints[to_go]>1:
            print('there are '+str(endpoints[to_go])+' such endpoints')
            check = input('print all if you want see it all and first to see first one:\n')
            if check == 'first':
                print(str(to_go)+ ':', find_endpoint(js, to_go))
            elif check == 'all':
                print(len(find_all_endpoints(js, to_go)))
                for elem in find_all_endpoints(js, to_go):
                    print(str(to_go)+ ':', elem)
        else:
            print(str(to_go)+ ':', find_endpoint(js, to_go))

    print('\n')
