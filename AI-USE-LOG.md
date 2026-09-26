## [2026-09-26] - إصلاح ZeroDivisionError وتغطية الاختبارات (Lab L2.2)

- **المشكلة ⚠️:** حدوث خلل `ZeroDivisionError: division by zero` في دالة `average_cost()` عند استدعائها لقائمة مهام فارغة.
- **الإصلاح المنجز 🛠️:** إضافة شرط للتحقق من وجود عناصر في القائمة `if not self.tasks: return 0.0` في ملف `tracker.py`.
- **التحقق والاختبار 🧪:**
  - إضافة اختبار `test_average_empty()` في ملف `test_tracker.py`.
  - تشغيل `pytest -q`: نجحت جميع الاختبارات (3 passed).
  - تقرير التغطية (`pytest-cov`): تغطية إجمالية للمشروع بنسبة **95%** (ملف `tracker.py` بنسبة 92%).