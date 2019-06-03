from mongoengine.document import  Document
from mongoengine import fields


# '交易号', '商家订单号', '交易创建时间', '付款时间', '最近修改时间', '交易来源地', '类型', '交易对方',
# '商品名称', '金额（元）', '收/支', '交易状态', '服务费（元）', '成功退款（元）', '备注', '资金状态'
class AliPayBillModel(Document):
    trade_no = fields.StringField(name="交易号")
    out_trade_no = fields.StringField(name="商家订单号")
    trade_create_time = fields.StringField(name="交易创建时间")
    payment_time = fields.StringField(name="付款时间")
    bill_update_time = fields.StringField(name="付款时间")
    trade_source = fields.StringField(name="交易来源地")
    trade_pay_type = fields.StringField(name="类型")
    counterparty = fields.StringField(name="交易对方")
    product_name = fields.StringField(name="商品名称")
    fee = fields.StringField(name="金额（元）")
    income_or_expense = fields.StringField(name="收/支")
    trade_state = fields.StringField(name="交易状态")
    service_fee = fields.StringField(name="服务费（元）")
    refund_fee = fields.StringField(name="成功退款（元）")
    remark = fields.StringField(name="备注")
    cash_status = fields.StringField(name="资金状态")

    meta = {
        "indexes": [],
        "index_background": True,
        "collection": "alipay_bill",
    }


# '交易时间', '交易类型', '交易对方', '商品', '收/支', '金额(元)', '支付方式', '当前状态', '交易单号', '商户单号', '备注'
class WechatPayBillModel(Document):
    trade_create_time = fields.StringField(name="交易时间")
    trade_pay_type = fields.StringField(name="交易时间")
    counterparty = fields.StringField(name="交易对方")
    product_name = fields.StringField(name="商品")
    income_or_expense = fields.StringField(name="收/支")
    fee = fields.StringField(name="金额（元）")
    pay_channel = fields.StringField(name="支付方式")
    trade_state = fields.StringField(name="当前状态")
    trade_no = fields.StringField(name="交易单号")
    out_trade_no = fields.StringField(name="商户单号")
    remark = fields.StringField(name="备注")

    meta = {
        "indexes": [],
        "index_background": True,
        "collection": "wechatpay_bill",
    }


class BillModel(Document):
    source = fields.StringField(name="账单来源")    # 微信导入/支付宝导入/信息收录
    title = fields.StringField(name="描述")
    fee = fields.DecimalField(name="金额（元）")
    remark = fields.StringField(name="备注")
    create_time = fields.DateTimeField("创建时间")
    is_delete = fields.BooleanField("删除")
    update_time = fields.DateTimeField("更新时间")

    meta = {
        "indexes": ["desc_type", "title"],
        "index_background": True,
        "collection": "file_info",
    }
