def inverter_string(s):
    string_invertida = ""
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string_original = "Olá mundo!"
string_invertida = inverter_string(string_original)

print(string_invertida)