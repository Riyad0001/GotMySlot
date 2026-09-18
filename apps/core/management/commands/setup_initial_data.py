from django.core.management.base import BaseCommand
from apps.core.models import (
    SiteSettings, HeroSection, HeroSlide,
    Service, ServiceFeature, WhyUsItem, FooterLink
)


class Command(BaseCommand):
    help = "Populate initial data for the visa slot booking website"

    def handle(self, *args, **options):
        self.stdout.write("Setting up initial data...")

        # ─── SiteSettings ──────────────────────────────────
        site, created = SiteSettings.objects.get_or_create(pk=1)
        site.agency_name = "Nasir Travel & Consultancy"
        site.site_name = "Nasir Travel & Consultancy"
        site.site_tagline = "Your Journey | Our Priority"
        site.phone = "+8801762364249"
        site.secondary_phone = "+8801620-855800"
        site.email = "travelnasir91@gmail.com"
        site.whatsapp_number = "+8801762364249"
        site.address = "House 70, Road 11, Block D, Banani, Dhaka"
        site.working_hours = "Sun-Thu : 9:00 AM - 8:00 PM"
        site.meta_title = "Nasir Travel & Consultancy | Visa & Travel Solutions"
        site.meta_description = "Fast, reliable, and hassle-free visa and travel support services across all countries with Nasir Travel & Consultancy."
        site.footer_about_text = "We provide fast, reliable, and hassle-free visa, ticket, tour, and travel support services with trusted professional guidance."
        site.copyright_text = "© 2026 Nasir Travel & Consultancy. All Rights Reserved."
        site.save()
        if created:
            self.stdout.write(self.style.SUCCESS("✓ SiteSettings created"))
        else:
            self.stdout.write("  SiteSettings already exists")

        # ─── HeroSection ───────────────────────────────────
        hero, created = HeroSection.objects.get_or_create(pk=1)
        if created:
            self.stdout.write(self.style.SUCCESS("✓ HeroSection created"))
        else:
            self.stdout.write("  HeroSection already exists")

        # ─── HeroSlides ────────────────────────────────────
        slides_data = [
            {"icon_class": "fas fa-passport", "title": "Visa Services", "subtitle": "Fast & Reliable", "order": 0},
            {"icon_class": "fas fa-plane", "title": "Travel Ready", "subtitle": "Book Your Slot Now", "order": 1},
            {"icon_class": "fas fa-globe-asia", "title": "All Centers", "subtitle": "Nationwide Coverage", "order": 2},
        ]
        if not HeroSlide.objects.exists():
            for data in slides_data:
                HeroSlide.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f"✓ {len(slides_data)} HeroSlides created"))
        else:
            self.stdout.write("  HeroSlides already exist")

        # ─── Services ──────────────────────────────────────
        services_data = [
            {
                "icon_class": "fas fa-briefcase-medical",
                "title": "Medical Visa",
                "price": 6000,
                "description": "Get your medical visa slot booked quickly for treatment in India.",
                "slot_rates": "IVAC Khulna: 6,000 TK\nIVAC Dhaka (JFP): 4,500 TK\nIVAC CTG: 7,000 TK\nIVAC Rajshahi: 4,500 TK\nIVAC Sylhet: 4,500 TK",
                "available_centers": "IVAC Khulna\nIVAC CTG\nIVAC Dhaka (JFP)\nIVAC Rajshahi\nIVAC Sylhet",
                "is_popular": False,
                "order": 0,
                "features": [
                    "IVAC Slot Booking",
                    "Application Assistance",
                    "Document Guidance",
                    "Fast Processing",
                    "Email Confirmation",
                ]
            },
            {
                "icon_class": "fas fa-suitcase-rolling",
                "title": "Tourist Visa",
                "price": 4000,
                "description": "Plan your India tour with our hassle-free tourist visa slot booking.",
                "slot_rates": "IVAC Khulna: 4,000 TK\nIVAC Dhaka (JFP): 3,500 TK\nIVAC CTG: 4,500 TK\nIVAC Rajshahi: 4,000 TK\nIVAC Sylhet: 3,000 TK",
                "available_centers": "IVAC Khulna\nIVAC CTG\nIVAC Dhaka (JFP)\nIVAC Rajshahi\nIVAC Sylhet",
                "is_popular": True,
                "order": 1,
                "features": [
                    "IVAC Slot Booking",
                    "Priority Processing",
                    "Document Checklist",
                    "Application Review",
                    "24/7 Support",
                    "Money Back Guarantee",
                ]
            },
            {
                "icon_class": "fas fa-passport",
                "title": "Double Entry Visa",
                "price": 19500,
                "description": "Secure your double entry visa slots for multiple visits to India.",
                "slot_rates": "IVAC Khulna: 6,500 TK\nIVAC Dhaka (JFP): 19,500 TK\nIVAC CTG: 17,500 TK\nIVAC Rajshahi: 16,500 TK\nIVAC Sylhet: 22,000 TK",
                "available_centers": "IVAC Khulna\nIVAC CTG\nIVAC Dhaka (JFP)\nIVAC Rajshahi\nIVAC Sylhet",
                "is_popular": False,
                "order": 2,
                "features": [
                    "IVAC Slot Booking",
                    "Premium Processing",
                    "Complete Document Assistance",
                    "Multiple Entry Support",
                    "Dedicated Agent",
                ]
            },
            {
                "icon_class": "fas fa-user-graduate",
                "title": "Student Visa",
                "price": 5000,
                "description": "Study in India with our student visa slot booking services for top universities.",
                "slot_rates": "IVAC Khulna: 4,500 TK\nIVAC Dhaka (JFP): 5,000 TK",
                "available_centers": "IVAC Khulna\nIVAC Dhaka (JFP)",
                "is_popular": False,
                "order": 3,
                "features": [
                    "Student Support",
                    "Document Review",
                    "Application Guidance",
                    "Appointment Booking",
                ]
            },
            {
                "icon_class": "fas fa-briefcase",
                "title": "Business Visa",
                "price": 10000,
                "description": "Expand your business with our business visa slot booking for India.",
                "slot_rates": "IVAC Khulna: 10,000 TK\nIVAC Dhaka (JFP): 5,000 TK",
                "available_centers": "IVAC Khulna\nIVAC Dhaka (JFP)",
                "is_popular": False,
                "order": 4,
                "features": [
                    "Fast Processing",
                    "Business Guidance",
                    "Documentation Support",
                    "Dedicated Assistance",
                ]
            },
            {
                "icon_class": "fas fa-house-user",
                "title": "Entry Visa",
                "price": 5500,
                "description": "Get your entry visa slot booked for visiting family or friends in India.",
                "slot_rates": "IVAC Khulna: 4,000 TK\nIVAC Dhaka (JFP): 5,500 TK",
                "available_centers": "IVAC Khulna\nIVAC Dhaka (JFP)",
                "is_popular": False,
                "order": 5,
                "features": [
                    "Family Visit Support",
                    "Fast Booking",
                    "Document Help",
                    "Friendly Guidance",
                ]
            },
        ]
        if Service.objects.count() < len(services_data):
            for sdata in services_data:
                features = sdata.pop("features")
                service, created = Service.objects.get_or_create(title=sdata["title"], defaults=sdata)
                if created:
                    for i, feat_text in enumerate(features):
                        ServiceFeature.objects.create(service=service, text=feat_text, order=i)
                else:
                    for field, value in sdata.items():
                        if field != "title":
                            setattr(service, field, value)
                    service.save()
                    ServiceFeature.objects.filter(service=service).delete()
                    for i, feat_text in enumerate(features):
                        ServiceFeature.objects.create(service=service, text=feat_text, order=i)
            self.stdout.write(self.style.SUCCESS(f"✓ {len(services_data)} Services with features created/updated"))
        else:
            self.stdout.write("  Services already exist")

        # ─── WhyUsItems ────────────────────────────────────
        why_data = [
            {"icon_class": "fas fa-clock", "title": "Quick Booking", "description": "Get your visa slot booked within 24 hours with our fast and efficient service.", "order": 0},
            {"icon_class": "fas fa-shield-alt", "title": "100% Secure", "description": "Your personal data and information are completely safe and secure with us.", "order": 1},
            {"icon_class": "fas fa-headset", "title": "24/7 Support", "description": "Our dedicated support team is always available to assist you anytime, anywhere.", "order": 2},
            {"icon_class": "fas fa-tags", "title": "Best Price", "description": "We offer competitive and transparent pricing with no hidden charges.", "order": 3},
        ]
        if WhyUsItem.objects.count() < len(why_data):
            for data in why_data:
                WhyUsItem.objects.get_or_create(title=data["title"], defaults=data)
            self.stdout.write(self.style.SUCCESS(f"✓ {len(why_data)} WhyUsItems created/updated"))
        else:
            self.stdout.write("  WhyUsItems already exist")

        # ─── FooterLinks ───────────────────────────────────
        links_data = [
            {"text": "Privacy Policy", "url": "#", "order": 0},
            {"text": "Terms of Service", "url": "#", "order": 1},
            {"text": "FAQ", "url": "#", "order": 2},
        ]
        if not FooterLink.objects.exists():
            for data in links_data:
                FooterLink.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f"✓ {len(links_data)} FooterLinks created"))
        else:
            self.stdout.write("  FooterLinks already exist")

        self.stdout.write(self.style.SUCCESS("\n✅ Initial data setup complete!"))
        self.stdout.write("   Visit /admin/ to customize all content.")
