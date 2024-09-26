import pytz
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTextEdit

class TimeConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta y campo para ingresar la fecha
        self.fecha_label = QLabel('Fecha (YYYY-MM-DD):', self)
        layout.addWidget(self.fecha_label)
        self.fecha_input = QLineEdit(self)
        layout.addWidget(self.fecha_input)

        # Etiqueta y campo para ingresar la hora
        self.hora_label = QLabel('Hora (HH:MM):', self)
        layout.addWidget(self.hora_label)
        self.hora_input = QLineEdit(self)
        layout.addWidget(self.hora_input)

        # Botón para convertir
        self.convertir_button = QPushButton('Convertir horas', self)
        layout.addWidget(self.convertir_button)
        self.convertir_button.clicked.connect(self.convertir_horas)

        # Campo de texto para mostrar y copiar el resultado
        self.resultado_text = QTextEdit(self)
        self.resultado_text.setReadOnly(True)  # Hacer que el campo solo permita lectura
        layout.addWidget(self.resultado_text)

        # Establecer el layout principal
        self.setLayout(layout)

        # Configuraciones básicas de la ventana
        self.setWindowTitle('Conversor de Horas Internacional')
        self.setGeometry(100, 100, 400, 300)

    def convertir_horas(self):
        fecha = self.fecha_input.text()
        hora = self.hora_input.text()

        try:
            datetime_str = f"{fecha} {hora}:00"  # Agregar segundos ":00"
            argentina_tz = pytz.timezone('America/Argentina/Buenos_Aires')
            argentina_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            argentina_time = argentina_tz.localize(argentina_time)
        except ValueError:
            QMessageBox.critical(self, "Error de formato", "Por favor, ingresa la fecha en formato YYYY-MM-DD y la hora en formato HH:MM")
            return

        # Convertir las horas a los otros países
        resultado = f"Hora ingresada en Argentina: {argentina_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        for country, tz in timezones.items():
            country_tz = pytz.timezone(tz)
            country_time = argentina_time.astimezone(country_tz)
            resultado += f"Hora en {country}: {country_time.strftime('%Y-%m-%d %H:%M:%S')}\n"

        # Mostrar el resultado en el campo de texto
        self.resultado_text.setText(resultado)

# Definir las zonas horarias de los países
timezones = {
    'Estados Unidos (New York)': 'America/New_York',
    'México (Ciudad de México)': 'America/Mexico_City',
    'Brasil (Sao Paulo)': 'America/Sao_Paulo',
    'España (Madrid)': 'Europe/Madrid',
    'China (Pekín)': 'Asia/Shanghai',
    'Colombia (Bogotá)': 'America/Bogota',
    'Chile (Santiago)': 'America/Santiago',
    'Perú (Lima)': 'America/Lima',
    'Venezuela (Caracas)': 'America/Caracas',
    'Uruguay (Montevideo)': 'America/Montevideo',
    'Paraguay (Asunción)': 'America/Asuncion',
    'Cuba (La Habana)': 'America/Havana',
    'Bolivia (La Paz)': 'America/La_Paz',
    'Ecuador (Quito)': 'America/Guayaquil',
    'Panamá (Ciudad de Panamá)': 'America/Panama',
    'República Dominicana (Santo Domingo)': 'America/Santo_Domingo'
}

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication([])
    window = TimeConverterApp()
    window.show()
    app.exec_()