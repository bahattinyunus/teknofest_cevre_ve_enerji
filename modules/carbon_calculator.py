"""
🌍 CarbonCalculator Module
ISO 14064 standartlarına göre emisyon hesaplamaları yapar.
"""

class CarbonCalculator:
    def __init__(self):
        # Türkiye elektrik şebekesi ortalama emisyon faktörü (örnek değer)
        self.emission_factor = 0.45  # kg CO2 / kWh

    def calculate_emissions(self, consumption_kwh):
        """Tüketilen enerji miktarını karbon emisyonuna dönüştürür."""
        return consumption_kwh * self.emission_factor

    def get_offset_recommendation(self, total_emissions):
        """Karbon dengeleme önerileri sunar."""
        pass
