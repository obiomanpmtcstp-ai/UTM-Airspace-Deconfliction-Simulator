"""
Candidate: Anyanwu Obioma Anselam
Project Component: Algorithmic Simulation of Dynamic Cylindrical Volume Exclusion (CVE) Adaptive Safety Scaling.
"""
import math
import time

class AnyanwuUTMSystem:
    def __init__(self, base_cve_radius_meters=50.0):
        self.base_radius = base_cve_radius_meters
        self.current_radius = base_cve_radius_meters
        self.adaptive_multiplier = 1.45
        
    def evaluate_airspace_safety(self, packet_loss_percentage):
        print(f"\n--- Checking Airspace Safety Status [Author: Anyanwu O.A.] ---")
        print(f"Current Network Telemetry Link Packet Loss: {packet_loss_percentage}%")
        
        if packet_loss_percentage == 0:
            self.current_radius = self.base_radius
            print(f"Status: NOMINAL (Ideal Environment)")
            print(f"Assigned CVE Radius Protection Envelope: {self.current_radius} meters")
            return "NOMINAL"
            
        elif packet_loss_percentage >= 40:
            print("Warning: Severe Link Drop Detected (The Nigerian Factor Environmental Constraint)")
            print("Action: Deploying Dynamic Adaptive Safety Scaling Override Logic...")
            
            # Apply the 1.45 x mathematical safety buffer blowout adjustment
            self.current_radius = self.base_radius * self.adaptive_multiplier
            
            print(f"Status: ADAPTIVE COMPENSATION DEPLOYED")
            print(f"New Dynamic CVE Protection Radius: {self.current_radius} meters (Expanded from {self.base_radius}m)")
            return "ADAPTIVE_ACTIVE"

def run_simulation_loop():
    # Initialize the engine block
    utm_engine = AnyanwuUTMSystem(base_cve_radius_meters=50.0)
    
    # 1. Simulate Baseline Environment 
    utm_engine.evaluate_airspace_safety(packet_loss_percentage=0)
    time.sleep(1)
    
    # 2. Inject Network Degradation Stressor
    utm_engine.evaluate_airspace_safety(packet_loss_percentage=40)

if __name__ == "__main__":
    run_simulation_loop()