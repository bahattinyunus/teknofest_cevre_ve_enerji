"""
🍃 GreenArchitect-TR: Elite Command Center - Main Entry Point
Hazırlayan: Bahattin Yunus Çetin
"""

import sys
import os
from modules.energy_analyzer import EnergyAnalyzer
from modules.iot_handler import IoTHandler
from modules.carbon_calculator import CarbonCalculator

def main():
    print("="*60)
    print("  🍃 GREENARCHITECT-TR: ELITE COMMAND CENTER INITIALIZED")
    print("  Architect: Bahattin Yunus Çetin")
    print("="*60)

    # Örnek Modül Isınma (Initialization)
    iot = IoTHandler(broker="mqtt.elite-energy.local")
    analyzer = EnergyAnalyzer()
    carbon = CarbonCalculator()

    print("\n[+] System Health Check: OK")
    print("[+] IoT Stream: Waiting for Data...")
    
    # Simüle edilmiş bir iş akışı
    current_load = 45.5 # kW
    prediction = analyzer.predict_next_hour(current_load)
    carbon_footprint = carbon.calculate_emissions(current_load)

    print(f"\n[📊] Güncel Yük: {current_load} kW")
    print(f"[🔮] 1 Saat Sonraki Tahmin: {prediction:.2f} kW")
    print(f"[🌍] Karbon Ayak İzi: {carbon_footprint:.2f} kg CO2/h")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
