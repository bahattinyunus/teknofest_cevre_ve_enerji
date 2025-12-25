"""
📡 IoTHandler Module
MQTT ve CoAP protokolleri üzerinden veri alışverişini yönetir.
"""

class IoTHandler:
    def __init__(self, broker="localhost", port=1883):
        self.broker = broker
        self.port = port
        print(f"[IoT] Connected to {self.broker}:{self.port}")

    def subscribe_to_sensors(self, topic="energy/meters/#"):
        """Sensör verilerini dinlemeye başlar."""
        print(f"[IoT] Subscribed to topic: {topic}")

    def publish_command(self, device_id, command):
        """Cihazlara (ör. Röleler) komut gönderir."""
        pass
