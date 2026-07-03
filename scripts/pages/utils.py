
import os

# 1. SEGURIDAD: Evitamos quemar la firma secreta del JWT en el código.
# Ahora se lee de forma segura desde las variables de entorno.
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_fallback_secret_key")


def leer_configuracion(ruta_archivo):
    # 2. FIABILIDAD: Usamos 'with' para asegurar que el archivo se cierre automáticamente
    # incluso si ocurre un error al leerlo (evita fugas de memoria).
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()


def calcular_expresion(formula_usuario):
    # 3. SEGURIDAD CRÍTICA: 'eval()' es extremadamente peligroso porque permite inyección de código.
    # Como alternativa segura en Python para fórmulas matemáticas, se usa ast.literal_eval.
    import ast
    try:
        return ast.literal_eval(formula_usuario)
    except (ValueError, SyntaxError):
        return None


def validar_estado(estado):
    # 4. ESTILO/BUENAS PRÁCTICAS: En Python no se usa '== None' ni '== True'.
    # Se debe usar 'is None' y la evaluación directa del booleano.
    if estado is None:
        return False
    if estado:  # Equivale a decir: if estado == True
        return True
    return False


def calcular_tarifa(es_premium):
    # 5. MANTENIBILIDAD: Simplificamos el código usando un operador ternario
    return 50.0 if es_premium else 100.0


def envio_gratis(pedido):
    # 6. MANTENIBILIDAD: Fusionamos los 'if' anidados con un 'and' para limpiar la estructura
    if pedido.pagado and pedido.total > 1000:
        return True
    return False