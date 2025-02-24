from django.contrib import messages
from django.shortcuts import get_object_or_404
# utils.py
from django.db import IntegrityError

def eliminar_registro(model, clave_primaria):
    try:
        # Obtener el objeto por su clave primaria
        objeto = model.objects.get(id=clave_primaria)
        objeto.delete()
        return True, f"Producto '{str(objeto)}' eliminado exitosamente."
    except model.DoesNotExist:
        return False, "Producto no encontrado."
    except IntegrityError:
        return False, "No se puede eliminar el producto debido a dependencias en otras entidades."
    except Exception as e:
        return False, f"Ocurrió un error al intentar eliminar el producto: {str(e)}"


def show_form_errors(request, forms):
    for form in forms:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"Error en {field}: {error}")