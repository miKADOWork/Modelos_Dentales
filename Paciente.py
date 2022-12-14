

def Pacientes_to_sql (file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            splited_client = lines.split()
            name = splited_client[0]
            surnames = splited_client[1] + " " + splited_client[2]
            
        
# Objeto paciente 
class Paciente:
    def __init__(self, name, apellidos, num_remo, num_ciru):
        self.nombre = name
        self.apellidos = apellidos
        self.num_modelos_removibles = num_remo
        self.num_modelos_cirujia = num_ciru

