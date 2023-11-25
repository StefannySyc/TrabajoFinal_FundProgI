import random

class Alumno:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado
    
    def __str__(self):
        return f"{self.codigo}: {self.nombre}, {self.estado}"
    
    def __repr__(self):
        return str(self)

class Curso:
    def __init__(self, codigo, nomCurso):
        self.codigo = codigo
        self.nomCurso = nomCurso
        self.nota = 0
    
    def __str__(self):
        return f"{self.codigo}: {self.nomCurso} ({self.nota})"
    
    def __repr__(self):
        return str(self)

def nomNota(lisCurso):
    return [x.nomCurso for x in lisCurso if x.nota >= 10]

def llenaDatos(lisCurso):
    cursos = ["Matemáticas", "Comunicación", "Ciencia y Tecnología"]
    for i, curso in enumerate(cursos, start=1):
        lisCurso.append(Curso(i, curso))
    
    for curso in lisCurso:
        curso.nota = random.randint(0, 20)

## MAIN
Cursos = []
llenaDatos(Cursos)

print("Cursos con notas:")
for curso in Cursos:
    print(curso)

notas_aprobadas = nomNota(Cursos)
print("\nCursos con notas mayores o iguales a 10:")
print(notas_aprobadas)
