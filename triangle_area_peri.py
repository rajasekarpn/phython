def tri_area_func(arg1,arg2,arg3):
    var_peri = (arg1 + arg2 + arg3)/2
    var_area = (var_peri*(var_peri-arg1) * (var_peri-arg2) * (var_peri-arg3)) ** 0.5
    return var_area
