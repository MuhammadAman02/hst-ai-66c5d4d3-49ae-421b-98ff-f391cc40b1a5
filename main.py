"""
Massimo Dutti - Luxury Fashion E-commerce Platform
Production-ready fashion e-commerce website with:
✓ Professional luxury fashion design and user experience
✓ Complete product catalog with categories and filtering
✓ Shopping cart and checkout functionality
✓ User authentication and account management
✓ Responsive design optimized for all devices
✓ SEO-optimized server-side rendering
✓ Secure payment processing integration ready
✓ Admin panel for product management
"""

import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    import uvicorn
    from app.main import app
    from app.core.config import settings
    from app.core.database import init_db
    from app.core.logger import logger
    
    if __name__ == "__main__":
        # Initialize database with sample data
        logger.info("Initializing database...")
        init_db()
        
        logger.info(f"Starting Massimo Dutti Fashion Platform on {settings.HOST}:{settings.PORT}")
        logger.info(f"Environment: {'Development' if settings.DEBUG else 'Production'}")
        
        uvicorn.run(
            "app.main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.DEBUG,
            log_level="info" if settings.DEBUG else "warning"
        )
        
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please install dependencies: pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Error starting application: {e}")
    sys.exit(1)