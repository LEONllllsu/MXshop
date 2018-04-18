from django.db import models
from DjangoUeditor.models import UEditorField

from datetime import datetime



# Create your models here.

class GoodsCategory(models.Model):

    CATEGOTY_TYPE=(
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目")
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别名code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGOTY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, verbose_name="父类别", help_text="父目录",
                                        related_query_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategotyBrand(models.Model):
    """
    品牌
    """
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="商品类别")
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="商品描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brand/images")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
    商品
    """

    category = models.ForeignKey(GoodsCategory, )
    good_sn = models.CharField()
    name = models.CharField()
    click_num = models.IntegerField()
    sold_num = models.IntegerField()
    fav_num = models.IntegerField()
    market_price = models.IntegerField()
    shop_price = models.IntegerField()
    goods_brief = models.TextField()
    goods_desc = UEditorField()
    ship_free = models.BooleanField()
    goods_front_image = models.ImageField(upload_to=)
    is_new = models.BooleanField()
    is_hot = models.BooleanField()
    add_time = models.DateTimeField(datetime.now)

class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey()
    image = models.ImageField(upload_to=)
    add_time = models.DateTimeField(datetime.now)

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods

class Banner(models.Model):
    """
    轮播商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to='banner',)
    index = models.IntegerField
    add_time = models.DateTimeField()

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name
