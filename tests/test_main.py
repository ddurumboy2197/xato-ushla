**Pytest**
```python
import pytest

def ushlovchi_dastur(x):
    if x == 0:
        raise ValueError("0 ga bo'lish xatoligi")
    return x / 0

def test_ushlovchi_dastur():
    with pytest.raises(ValueError):
        ushlovchi_dastur(0)

def test_ushlovchi_dastur_samimiy():
    assert ushlovchi_dastur(1) == float('inf')
```

**Jest**
```javascript
describe('ushlovchiDastur', () => {
    it('0 ga bo\'lish xatoligini ushlovchi', () => {
        expect(() => ushlovchiDastur(0)).toThrowError('0 ga bo\'lish xatoligi');
    });

    it('0 ga bo\'lish xatoligini ushlovchisiz', () => {
        expect(ushlovchiDastur(1)).toBe(Infinity);
    });
});

function ushlovchiDastur(x) {
    if (x === 0) {
        throw new Error('0 ga bo\'lish xatoligi');
    }
    return 1 / x;
}
```
