import json

def trans_to_json(text_name):
    print('text name : ' + text_name)
    file = open(text_name, mode='r')

    result_dic = {}
    result_dic['data'] = []

    header = file.readline().rstrip('\n').split()

    for line in file:
        line_word = line.rstrip('\n').split('\t')
        temp_dict = {}
        for i in range(len(line_word)):
            temp_dict[header[i]] = line_word[i]
        result_dic['data'].append(temp_dict)

    file.close()

    return result_dic


'''
    print(json.dumps(result_dic, ensure_ascii=False, indent='\t'))
    print("!")

    file = open('./data/json/' + json_name, mode='w')
    file.write(json.dumps(result_dic, ensure_ascii=False, indent='\t'))
    file.close()
'''