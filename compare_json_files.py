import json

def get_main_array(data):
    for key, value in data.items():
        if isinstance(value, list):
            return value
    return None

def get_name(path):
    return path.split("\\")[-1]


def compare_json_files(data1, data2):
    divergencias_encontradas = False

    array1 = get_main_array(data1)
    array2 = get_main_array(data2)

    if array1 is None or array2 is None:
        print("Um ou ambos os arquivos JSON não contêm um array principal como esperado.")
        return
    if len(array1) != len(array2):
        print("Os JSONs possuem números diferentes de objetos no array principal.")
        return

    print(f"\nHá {len(array1)} objetos no array principal.")
    header_printed = False  # Inicialize a variável


    for i in range(len(array1)):
        obj1 = array1[i]
        obj2 = array2[i]

        widths = [
            max(len(key) for key in obj1.keys()),
            max(len(str(value)) for value in obj1.values()),  
            max(len(str(value)) for value in obj2.values())   
        ]

        for key, value in obj1.items():
            if key in obj2:
                is_zero_none_divergence = (value == 0 and obj2[key] is None) or (value is None and obj2[key] == 0)
                if obj2[key] != value and not is_zero_none_divergence:
                    divergencias_encontradas = True
                    name1 = get_name(file_path1)
                    name2 = get_name(file_path2)

                    if i > 0:
                        print(f"Objeto {i}, Chave: {key}, Valor --> {name1}: {value}, Valor --> {name2}: {obj2[key]}")
                    else:
                        if not header_printed:
                            print(f"{'Chave':<{widths[0]}}  {name1:<{widths[1]}}  {name2:<{widths[2]}}")
                            header_printed = True
                        print(f"{key if key is not None else 'None':<{widths[0]}}  {str(value) if value is not None else 'None':<{widths[1]}}  {str(obj2[key]) if obj2[key] is not None else 'None':<{widths[2]}}")



    if not divergencias_encontradas:
        print("Sem divergencias encontradas")

if __name__ == '__main__':
    file_path1 = input('Enter the path to the first JSON file WITHOUT PARENTSIS \"\": ')
    file_path2 = input('Enter the path to the second JSON file WITHOUT PARENTSIS \"\": ')

    with open(file_path1, 'r') as f1:
        data1 = json.load(f1)

    with open(file_path2, 'r') as f2:
        data2 = json.load(f2)

    compare_json_files(data1, data2)
