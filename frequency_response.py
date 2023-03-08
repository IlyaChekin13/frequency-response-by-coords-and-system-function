import math
import numpy as np
import pandas as pd
import re


EXCEL_PATH = "data.xlsx"

def frequency_response(N, P):

    circle_coords = []
    N_val = []
    P_val = []


    for i in range(361):
        x = math.cos(i * math.pi / 180)
        y = math.sin(i * math.pi / 180)
        circle_coords.append([x,y])
 
    for cc in circle_coords:
        b = []
        for el in N:
            b.append(math.sqrt((cc[0] - el[0])**2 + (cc[1] - el[1])**2))
        N_val.append(np.prod(b))

    for cc in circle_coords:
        b = []
        for el in P:
            b.append(math.sqrt((cc[0] - el[0])**2 + (cc[1] - el[1])**2))
        P_val.append(np.prod(b))

    res = [N_val[i] / P_val[i] for i in range(len(N_val))]
    
    return res


def get_zeros_and_poles_from_input():

    N_coords = []
    P_coords = []

    print("Ввод нулей\nДля завершения ввода, введите пустое значение.")

    while True:
        inp = list()
        inp.append(input("Введи кординату x \n>"))
        if inp[0] == "":
            break
        inp.append(input("Введи кординат y \n>"))
        N_coords.append([float(inp[0]), float(inp[1])])

    print("Ввод полюсов\nДля завершения ввода, введите пустое значение.")

    while True:
    
        inp = list()
        inp.append(input("Введи кординату x \n>"))
        if inp[0] == "":
            break
        inp.append(input("Введи кординат y \n>"))
        P_coords.append([float(inp[0]), float(inp[1])])
    
    return N_coords, P_coords


def import_to_excel(data, excel_path):
    pd.DataFrame(data).to_excel(excel_path)
    

def get_zeros_and_poles_coordinates():
    coefs_n = re.findall(r"-?\d+[\.\d+]*", input("Введите коэффициенты уравнения числителя (через пробел) > "))
    roots_n = np.roots(coefs_n[::-1])
    N_coords = [[roots_n[i].real,roots_n[i].imag] for i in range(len(roots_n))]
    coefs_p = re.findall(r"-?\d+[\.\d+]*", input("Введите коэффициенты уравнения знаменателя (через пробел) > "))
    roots_p = np.roots(coefs_p[::-1])
    print(f"{roots_n} - корни числителя \n{roots_p} - корни знаменателя")
    P_coords = [[roots_p[i].real,roots_p[i].imag] for i in range(len(roots_p))]
    
    return N_coords, P_coords 

def main():
    choice = int(input("Ввести системную функцию - 1\nВвести координаты нулей и полюсов - 2\n>"))
    if choice == 1:
        coords = get_zeros_and_poles_coordinates()
    else:
        coords = get_zeros_and_poles_from_input()
    import_to_excel(frequency_response(coords[0], coords[1]), EXCEL_PATH)
    print(f"Данные записаны в {EXCEL_PATH}")


if __name__ == "__main__":
    main()